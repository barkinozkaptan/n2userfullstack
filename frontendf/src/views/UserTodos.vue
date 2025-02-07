<template>
  <div class="flex h-screen pt-8">
    <!-- Main Content -->
    <div class="w-full p-6">
      <!-- Button Container (Go Back & Save Changes aligned) -->
      <div class="flex justify-between items-center mb-4">
        <!-- Go Back Button (Left) -->
        <GoBackButton routeName="Home" buttonLabel="Go to Home" />
        
        <!-- Save Changes Button (Right) -->
        <button @click="saveChanges"
          class="px-4 py-2 bg-purple-700 text-white text-md rounded-lg hover:bg-purple-800 transition duration-300">
          Save Changes
        </button>
      </div>

      <!-- Todos List -->
      <ul>
        <li v-for="todo in todos" :key="todo.id" class="flex items-center p-3 border-b border-gray-300">
          <!-- Checkbox to toggle completed status -->
          <input type="checkbox" :checked="todo.completed" @change="toggleTodo(todo.id)"
            class="mr-4 accent-purple-700 w-5 h-5" />
          <!-- Display the todo title -->
          <span class="text-gray-900 font-medium text-md">
            {{ formatTitle(todo.title) }}
          </span>
        </li>
      </ul>

      <!-- No todos message -->
      <p v-if="todos.length === 0" class="text-gray-500 mt-4">
        No tasks available for this user.
      </p>
    </div>

    <!-- Modal -->
    <div v-if="showModal" class="fixed inset-0 flex items-start justify-center bg-black bg-opacity-50 pt-10">
      <div class="bg-white p-6 rounded-lg shadow-lg w-1/3 flex flex-col items-center">
        <h2 class="text-lg font-semibold mb-4">{{ modalTitle }}</h2>
        <p class="text-gray-700 text-center">{{ modalMessage }}</p>
        <button @click="closeModal"
          class="mt-4 px-4 py-2 bg-purple-700 text-white rounded-md hover:bg-purple-800 transition">
          Close
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import GoBackButton from "@/components/GoBackButton.vue"; // Import GoBackButton component
import service from "@/services/service"; // Import Axios service instance

export default {
  name: "UserTodos",
  props: {
    id: {
      type: Number,
      required: false, // Allows using either a prop or a route param
    },
  },
  data() {
    return {
      todos: [], // Stores the todos fetched from the API
      showModal: false, // Controls modal visibility
      modalTitle: "", // Modal title
      modalMessage: "" // Modal message
    };
  },
  computed: {
    userId() {
      return this.id || this.$route.params.id;
    },
  },
  components: {
    GoBackButton,
  },
  mounted() {
    this.fetchTodos(); // ✅ Now Vue will correctly find the function
  },
  methods: {
    // Fetch todos for the specific user
    async fetchTodos() {
      try {
        const response = await service.get(`/tasks/user/${this.userId}/`);
        
        console.log("🔍 API Response:", response.data); // ✅ Debugging output

        if (response.data.source === "redis") {
            console.log("✅ Todos fetched from Redis cache:", response.data.data);
        } else {
            console.log("📌 Todos fetched from database:", response.data.data);
        }

        this.todos = Array.isArray(response.data.data) ? response.data.data.sort((a, b) => a.id - b.id) : [];
      } catch (error) {
        console.error("❌ Error fetching todos:", error);
        this.todos = [];
      }
    },
    // Toggle the completed status of a task
    toggleTodo(id) {
      const todo = this.todos.find((t) => t.id === id);
      if (todo) {
        todo.completed = !todo.completed;
      }
    },
    // Save updated todos to the backend
    async saveChanges() {
    try {
        for (const todo of this.todos) {
            await service.put(`/tasks/${todo.id}/`, {
                title: todo.title, // Include title
                user: todo.user,   // Include user
                completed: todo.completed
            });
        }
        
        console.log("✅ Tasks updated successfully! Refreshing Redis data...");
        this.showModalWithMessage("Success", "Changes saved successfully!");

        // ✅ After updating tasks, refetch the updated data from Redis
        setTimeout(() => {
            this.fetchTodos();
        }, 1000); // Give a slight delay before re-fetching from cache
    } catch (error) {
        console.error("❌ Error updating todos:", error.response ? error.response.data : error.message);
        this.showModalWithMessage("Error", "Failed to save changes.");
    }
}
,
    // Display modal with a message
    showModalWithMessage(title, message) {
      this.modalTitle = title;
      this.modalMessage = message;
      this.showModal = true;
    },
    // Close modal
    closeModal() {
      this.showModal = false;
    },
    // Format the title to start with an uppercase letter
    formatTitle(title) {
      return title.charAt(0).toUpperCase() + title.slice(1);
    },
  },
};
</script>

<style scoped>
body {
  font-family: "Arial", sans-serif;
}
</style>
