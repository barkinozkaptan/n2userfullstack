
<template>
  <div class="flex h-screen">
    <aside
      class="bg-gray-200 text-gray-600 flex flex-col fixed left-0 top-0 h-full overflow-y-auto transition-all duration-300"
      :class="{
        'w-64': !isCollapsed,
        'w-20': isCollapsed
      }"
    >
      <nav class="flex-grow py-8 border border-gray-300 flex flex-col justify-between">
        <div v-if="user && user.id" class="flex items-center mb-8 px-4 pb-8 border-b border-gray-300">
  <img
    :src="`https://i.pravatar.cc/150?img=${user.id}`"
    alt="Profile Picture"
    class="w-12 h-12 rounded-full"
  />
  <div v-if="!isCollapsed" class="ml-4 w-full">
    <h1 class="text-lg font-semibold text-gray-800 break-words w-full">{{ user.name }}</h1>
    <p class="text-sm text-gray-500 break-words w-full">{{ user.email }}</p>
  </div>
</div>
        <p v-if="!user || !user.id" class="text-center text-gray-500">Select a user to view details</p>

        <ul>
          <li
            v-for="link in links"
            :key="link.path"
            class="mb-4 py-1 relative flex items-center"
            :class="{ 'justify-center': isCollapsed }"
          >
            <div
              v-if="isActive(link.path)"
              class="absolute inset-y-0 left-0 w-2 bg-purple-700 rounded-right-custom"
            ></div>
            <router-link
              :to="`/user/${user.id}${link.path}`"
              class="flex items-center ml-6"
              :class="{ 'text-purple-700': isActive(link.path), 'ml-0': isCollapsed }"
              v-if="user && user.id"
            >
              <span v-html="link.icon" class="w-6 h-6"></span>
              <p v-if="!isCollapsed" class="text-md ml-4">{{ link.name }}</p>
            </router-link>
          </li>
        </ul>

        <div class="h-16 flex items-center justify-center border-t pt-6 border-gray-300 mt-auto">
          <img src="@/assets/image.png" alt="" class="w-10 h-10" />
          <h1 v-if="!isCollapsed" class="text-xl font-bold ml-1">N2Mobil</h1>
        </div>
      </nav>
    </aside>

    <main class="flex-grow p-4" :class="{ 'ml-64': !isCollapsed, 'ml-20': isCollapsed }">
      <slot></slot>
    </main>
  </div>
</template>

<script>
export default {
  name: "Header2",
  props: {
    user: {
      type: Object,
      required: false,
      default: () => ({}),
    },
  },
  data() {
    return {
      isCollapsed: false,
      links: [
        {
          name: "Todos",
          path: "/todos",
          icon: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M9 5H7C6.46957 5 5.96086 5.21071 5.58579 5.58579C5.21071 5.96086 5 6.46957 5 7V19C5 19.5304 5.21071 20.0391 5.58579 20.4142C5.96086 20.7893 6.46957 21 7 21H17C17.5304 21 18.0391 20.7893 18.4142 20.4142C18.7893 20.0391 19 19.5304 19 19V7C19 6.46957 18.7893 5.96086 18.4142 5.58579C18.0391 5.21071 17.5304 5 17 5H15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M9 14H9.01M9 17H9.01M12 16L13 17L16 14M9 5C9 4.46957 9.21071 3.96086 9.58579 3.58579C9.96086 3.21071 10.4696 3 11 3H13C13.5304 3 14.0391 3.21071 14.4142 3.58579C14.7893 3.96086 15 4.46957 15 5C15 5.53043 14.7893 6.03914 14.4142 6.41421C14.0391 6.78929 13.5304 7 13 7H11C10.4696 7 9.96086 6.78929 9.58579 6.41421C9.21071 6.03914 9 5.53043 9 5Z" stroke="#4F359B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>`
        },
        {
          name: "Posts",
          path: "/posts",
          icon: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M9 4V22M13 8H15M13 12H15M6 4H17C17.5304 4 18.0391 4.21071 18.4142 4.58579C18.7893 4.96086 19 5.46957 19 6V18C19 18.5304 18.7893 19.0391 18.4142 19.4142C18.0391 19.7893 17.5304 20 17 20H6C5.73478 20 5.48043 19.8946 5.29289 19.7071C5.10536 19.5196 5 19.2652 5 19V5C5 4.73478 5.10536 4.48043 5.29289 4.29289C5.48043 4.10536 5.73478 4 6 4Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>`
        },
        {
          name: "Albums",
          path: "/albums",
          icon: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M15 8H15.01M11.5 21H6C5.20435 21 4.44129 20.6839 3.87868 20.1213C3.31607 19.5587 3 18.7956 3 18V6C3 5.20435 3.31607 4.44129 3.87868 3.87868C4.44129 3.31607 5.20435 3 6 3H18C18.7956 3 19.5587 3.31607 20.1213 3.87868C20.6839 4.44129 21 5.20435 21 6V11" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M3 16L8 11C8.928 10.107 10.072 10.107 11 11L12.5 12.5M18 22L21.35 18.716C21.5554 18.5166 21.7188 18.2782 21.8306 18.0146C21.9423 17.7511 22.0001 17.4678 22.0006 17.1816C22.0011 16.8953 21.9442 16.6118 21.8333 16.3479C21.7224 16.084 21.5598 15.845 21.355 15.645C20.9371 15.2363 20.3762 15.007 19.7917 15.0059C19.2072 15.0048 18.6454 15.2319 18.226 15.639L18.002 15.859L17.779 15.639C17.3612 15.2306 16.8005 15.0015 16.2162 15.0004C15.632 14.9993 15.0704 15.2262 14.651 15.633C14.4455 15.8323 14.282 16.0707 14.1702 16.3342C14.0583 16.5977 14.0004 16.881 13.9999 17.1672C13.9993 17.4535 14.0561 17.737 14.1669 18.0009C14.2777 18.2648 14.4403 18.5039 14.645 18.704L18 22Z" stroke="#4F359B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>`
        }
      ]
    };
  },
  mounted() {
    const mediaQuery = window.matchMedia("(max-width: 768px)");
    this.isCollapsed = mediaQuery.matches;
    mediaQuery.addEventListener("change", (e) => {
      this.isCollapsed = e.matches;
    });
  },
  methods: {
    isActive(path) {
      return this.$route.path.includes(path);
    },
  },
};
</script>
