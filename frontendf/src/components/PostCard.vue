<template>
    <li class="bg-white px-12 pb-12 pt-2 border-b border-gray-200 relative">
      <div class="flex flex-col space-y-4">
        <!-- Format the title using a local method -->
        <h3 class="text-xl text-neutral-900">{{ formatTitle(post.title) }}</h3>
        <p class="text-gray-600 leading-relaxed w-3/4 text-md line-clamp-2">
          {{ post.body }}
        </p>
      </div>
  
      <!-- Emit openModal event to parent, passing post's id -->
      <button
        @click="onOpenModal"
        class="absolute bottom-4 right-4 flex items-center text-purple-700 font-semibold hover:text-purple-900"
      >
        See More
        <svg
          width="32"
          height="32"
          viewBox="0 0 32 32"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          class="ml-1"
        >
          <path
            d="M16 20L20 16M20 16L16 12M20 16H12"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M16 7C23.2 7 25 8.8 25 16C25 23.2 23.2 25 16 25C8.8 25 7 23.2 7 16C7 8.8 8.8 7 16 7Z"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
      </button>
    </li>
  </template>
  
  <script>
  export default {
    name: "PostCard",
    props: {
      post: {
        type: Object,
        required: true,
      },
    },
    methods: {
      formatTitle(title) {
        // Capitalize the first letter of the title
        return title.charAt(0).toUpperCase() + title.slice(1);
      },
      onOpenModal() {
        // Emit an event to the parent so it can open the modal
        this.$emit("openModal", this.post.id);
      },
    },
  };
  </script>
  
  <style scoped>
  /* Scoped styles for the post card can go here, if needed */
  </style>
  