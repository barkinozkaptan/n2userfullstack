<template>
  <div>
    <UserCard :users="users" @user-selected="selectUser" />
  </div>
</template>

<script>
import UserCard from "../components/UserCard.vue";
import service from "@/services/service";

export default {
  name: "HomePage",
  components: {
    UserCard,
  },
  data() {
    return {
      users: [], // Holds the fetched users
    };
  },
  async mounted() {
    await this.fetchUsers();
  },
  methods: {
    async fetchUsers() {
  try {
    const response = await service.get("/users/");
    
    if (response.data && Array.isArray(response.data.data)) {
      this.users = response.data.data.sort((a, b) => a.id - b.id);
      console.log("Data fetched from:", response.data.source); // ✅ Log the source
    } else {
      console.error("Unexpected API response format:", response.data);
      this.users = [];
    }
  } catch (error) {
    console.error("Error fetching users:", error);
    this.users = [];
  }
}
,
    selectUser(user) {
      // Emit the event to the parent (App.vue)
      this.$emit("user-selected", user);
      // Navigate to the user's todos
      this.$router.push({ name: "UserTodos", params: { id: user.id } });
    },
  },
};
</script>