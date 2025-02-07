


   <template>
    <div class="flex h-screen">
      <aside
        class="bg-gray-200 text-gray-600 flex flex-col fixed left-0 top-0 h-screen overflow-y-auto transition-all duration-300"
        :class="{
          'w-64': !isCollapsed,
          'w-20': isCollapsed
        }"
      >
        <nav class="flex-grow py-8 border border-gray-300 flex flex-col justify-between">
          <ul>
            <li
              class="mb-4 bg-white py-1 pl-4 flex items-center relative"
              :class="{
                'pl-4': !isCollapsed,
                'pl-0 justify-center': isCollapsed
              }"
            >
              <div
                class="absolute inset-y-0 left-0 w-1.5 bg-purple-700 rounded-right-custom"
                v-if="!isCollapsed"
              ></div>
              <a
                href="#"
                class="flex items-center text-purple-700 ml-4"
                :class="{ 'ml-0': isCollapsed }"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path d="M9 7m-4 0a4 4 0 1 0 8 0a4 4 0 1 0 -8 0" />
                  <path d="M3 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2" />
                  <path d="M16 3.13a4 4 0 0 1 0 7.75" />
                  <path d="M21 21v-2a4 4 0 0 0 -3 -3.85" />
                </svg>
                <p
                  v-if="!isCollapsed"
                  class="text-md ml-4 transition-opacity duration-300"
                >
                  Users
                </p>
              </a>
            </li>
          </ul>
          <div
            class="h-16 flex items-center justify-center border-t pt-6 border-gray-300 mt-auto"
          >
            <img
              v-if="!isCollapsed"
              src="@/assets/image.png"
              alt=""
              class="w-10 h-10"
            />
            <h1
              v-if="!isCollapsed"
              class="text-xl font-bold ml-1 transition-opacity duration-300"
            >
              N2Mobil
            </h1>
          </div>
        </nav>
      </aside>
  
      <main class="flex-grow p-4" :class="{ 'ml-64': !isCollapsed, 'ml-20': isCollapsed }">
        <!-- Main content -->
      </main>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isCollapsed: false
      };
    },
    mounted() {
      const mediaQuery = window.matchMedia("(max-width: 768px)");
      this.isCollapsed = mediaQuery.matches;
      mediaQuery.addEventListener("change", (e) => {
        this.isCollapsed = e.matches;
      });
    }
  };
  </script>
  
  <style>
  .bg-purple-700 {
    background-color: #6b46c1;
  }
  
  .rounded-right-custom {
    border-top-right-radius: 12px;
    border-bottom-right-radius: 12px;
  }
  </style>
  