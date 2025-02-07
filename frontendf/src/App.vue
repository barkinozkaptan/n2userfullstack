<template>
  <div class="flex h-screen">
    <!-- Conditional Header with currentUser Prop -->
    <component :is="currentHeader" :user="currentUser" />
    <main class="flex-grow">
      <router-view @user-selected="updateCurrentUser" @clear-selection="clearCurrentUser" />
    </main>
  </div>
</template>

<script>
import { reactive, ref, watch, onMounted } from "vue";
import { useRoute } from "vue-router";
import Header from "./components/Header.vue";
import Header2 from "./components/Header2.vue";

export default {
  name: "App",
  components: {
    Header,
    Header2,
  },
  setup() {
    const currentUser = reactive({}); // Holds the current selected user
    const currentHeader = ref("Header"); // Default to Header
    const route = useRoute();

    const updateCurrentUser = (user) => {
      if (user && user.id) {
        // Set the new user and switch to Header2
        Object.assign(currentUser, user);
        currentHeader.value = "Header2";
        localStorage.setItem("selectedUser", JSON.stringify(user)); // Persist the user
      }
    };

    const clearCurrentUser = () => {
      // Clear the user and reset to Header
      Object.assign(currentUser, {});
      currentHeader.value = "Header";
      localStorage.removeItem("selectedUser");
    };

    // Watch for route changes and reset header if user is cleared
    watch(
      () => route.path,
      () => {
        if (!localStorage.getItem("selectedUser")) {
          clearCurrentUser();
        }
      }
    );

    onMounted(() => {
      // Restore the user from localStorage on app load
      const storedUser = localStorage.getItem("selectedUser");
      if (storedUser) {
        const user = JSON.parse(storedUser);
        Object.assign(currentUser, user);
        currentHeader.value = "Header2";
      }
    });

    return {
      currentUser,
      currentHeader,
      updateCurrentUser,
      clearCurrentUser,
    };
  },
};
</script>
