<!-- <template>
  <button class="flex items-center text-gray-600 mb-4" @click="goBack">
    <svg
      width="32"
      height="32"
      viewBox="0 0 32 32"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M16 10.6667L10.6667 16M10.6667 16L16 21.3333M10.6667 16H21.3333"
        stroke="#26303E"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
      <path
        d="M16 4C25.6 4 28 6.4 28 16C28 25.6 25.6 28 16 28C6.4 28 4 25.6 4 16C4 6.4 6.4 4 16 4Z"
        stroke="#26303E"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
    </svg>
    <span class="text-gray-800 font-semibold text-md ml-4">{{ buttonLabel }}</span>
  </button>
</template>

<script>
export default {
  name: "GoBackButton",
  props: {
    /**
     * The route name you want to push to.
     * e.g. 'Home', 'Albums', 'UserTodos', etc.
     */
    routeName: {
      type: String,
      required: true,
    },
    /**
     * (Optional) route params if needed, e.g. { id: 123 }
     */
    routeParams: {
      type: Object,
      default: () => ({}),
    },
    /**
     * The label text next to the icon.
     */
    buttonLabel: {
      type: String,
      default: "Go Back",
    },
  },
  methods: {
    goBack() {
      // Clear the current user selection
      localStorage.removeItem("selectedUser");
      this.$emit('user-selected', null); // Notify parent to clear currentUser

      // On click, push to the route given in the props
      // Pass in the name and any params you might have
      this.$router.push({
        name: this.routeName,
        params: this.routeParams,
      });
    },
  },
};
</script>

<style scoped>
/* Your button-specific styles can go here */
</style> -->

<template>
  <button class="flex items-center text-gray-600 mb-4" @click="goBack">
    <svg
      width="32"
      height="32"
      viewBox="0 0 32 32"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M16 10.6667L10.6667 16M10.6667 16L16 21.3333M10.6667 16H21.3333"
        stroke="#26303E"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
      <path
        d="M16 4C25.6 4 28 6.4 28 16C28 25.6 25.6 28 16 28C6.4 28 4 25.6 4 16C4 6.4 6.4 4 16 4Z"
        stroke="#26303E"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
    </svg>
    <span class="text-gray-800 font-semibold text-md ml-4">{{ buttonLabel }}</span>
  </button>
</template>

<script>
export default {
  name: "GoBackButton",
  props: {
    /**
     * The route name you want to push to.
     * e.g. 'Home', 'Albums', 'UserTodos', etc.
     */
    routeName: {
      type: String,
      required: true,
    },
    /**
     * (Optional) route params if needed, e.g. { id: 123 }
     */
    routeParams: {
      type: Object,
      default: () => ({}),
    },
    /**
     * The label text next to the icon.
     */
    buttonLabel: {
      type: String,
      default: "Go Back",
    },
  },
  methods: {
    goBack() {
      // Clear the user selection only if navigating away from Albums
      if (this.routeName !== "Albums") {
        localStorage.removeItem("selectedUser");
        this.$emit("user-selected", null); // Notify parent to clear currentUser
      }

      // On click, push to the route given in the props
      this.$router.push({
        name: this.routeName,
        params: this.routeParams,
      });
    },
  },
};
</script>

<style scoped>
/* Your button-specific styles can go here */
</style>
