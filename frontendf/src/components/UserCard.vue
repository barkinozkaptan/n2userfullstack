<template>
  <div class="py-8 pr-8">
    <h2 class="text-xl font-semibold mb-6 text-gray-800">All Users</h2>

    <div v-if="users.length === 0" class="text-center text-gray-500">
      No users found.
    </div>

    <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-6">
      <div v-for="user in users" :key="user.id"
        class="bg-white border border-gray-300 rounded-lg shadow-lg p-6 flex flex-col h-auto transform transition-transform duration-300 hover:scale-105 cursor-pointer"
        @click="$emit('user-selected', user)">
        <div class="flex items-center mb-6">
          <img :src="`https://i.pravatar.cc/150?img=${user.id}`" alt="User Avatar"
            class="w-20 h-20 sm:w-28 sm:h-28 rounded-full mr-4" />
          <div class="flex-1 overflow-hidden">
            <h3 class="text-lg font-semibold text-gray-800 truncate">{{ user.name }}</h3>
            <p class="text-sm text-gray-500 truncate">{{ user.email }}</p>
            <p class="text-sm text-gray-500 truncate">{{ user.phone }}</p>
          </div>
        </div>

        <div class="text-sm text-gray-600 flex-1">
          <p class="mb-2 flex items-center">
            <svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M15.3333 10.9998C15.3331 10.4486 15.181 9.9082 14.8939 9.43777C14.6067 8.96735 14.1954 8.58514 13.7053 8.33308C13.2151 8.08102 12.665 7.96886 12.1153 8.00891C11.5656 8.04896 11.0376 8.23967 10.5891 8.56011C10.1407 8.88055 9.7892 9.31834 9.57323 9.82542C9.35725 10.3325 9.28515 10.8893 9.36482 11.4347C9.4445 11.98 9.67287 12.4929 10.0249 12.917C10.3769 13.3411 10.8389 13.66 11.3603 13.8388"
                stroke="#26303E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
              <path
                d="M12.0933 21.4699C11.6494 21.417 11.2362 21.2162 10.9203 20.8999L6.67631 16.6569C5.74408 15.7245 5.05674 14.5762 4.67545 13.3141C4.29415 12.0519 4.23071 10.7151 4.49077 9.42254C4.75083 8.12997 5.32633 6.92171 6.16607 5.90524C7.00582 4.88877 8.08378 4.09561 9.30405 3.59631C10.5243 3.09702 11.8491 2.90706 13.1605 3.04334C14.4719 3.17962 15.7293 3.63792 16.8209 4.37746C17.9124 5.11701 18.8042 6.11487 19.417 7.28229C20.0298 8.4497 20.3446 9.75048 20.3333 11.0689"
                stroke="#26303E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
              <path
                d="M18.3333 21.9999L21.6833 18.7159C21.8887 18.5165 22.0522 18.278 22.1639 18.0145C22.2756 17.7509 22.3335 17.4677 22.3339 17.1814C22.3344 16.8952 22.2775 16.6117 22.1666 16.3478C22.0557 16.0839 21.8931 15.8449 21.6883 15.6449C21.2704 15.2362 20.7095 15.0069 20.125 15.0058C19.5406 15.0046 18.9787 15.2318 18.5593 15.6389L18.3353 15.8589L18.1123 15.6389C17.6945 15.2305 17.1338 15.0014 16.5495 15.0002C15.9653 14.9991 15.4037 15.2261 14.9843 15.6329C14.7788 15.8321 14.6153 16.0706 14.5035 16.3341C14.3917 16.5976 14.3338 16.8808 14.3332 17.1671C14.3326 17.4534 14.3894 17.7368 14.5002 18.0008C14.611 18.2647 14.7736 18.5038 14.9783 18.7039L18.3333 21.9999Z"
                stroke="#26303E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            </svg>

            <span class="ml-2">Location:</span>
          </p>
          <span class="block mb-4 font-extralight break-words">
            {{ user.address.street }}, {{ user.address.city }}
          </span>

          <p class="mb-2 flex items-center">
            <svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M3.33331 21H21.3333M5.33331 21V7L13.3333 3V21M19.3333 21V11L13.3333 7M9.33331 9V9.01M9.33331 12V12.01M9.33331 15V15.01M9.33331 18V18.01"
                stroke="#26303E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            </svg>

            <span class="ml-2">Company:</span>
          </p>
          <span class="block mb-4 font-extralight break-words">{{ user.company.name }}</span>

          <p class="flex mb-2 items-center">
            <svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M21.2733 13.045C21.4851 11.2333 21.1414 9.39995 20.2877 7.78798C19.4341 6.176 18.1107 4.86147 16.4931 4.01857C14.8755 3.17566 13.0399 2.84418 11.2296 3.06805C9.41935 3.29191 7.71983 4.06055 6.35626 5.27212C4.9927 6.48369 4.02946 8.08099 3.59418 9.85236C3.15891 11.6237 3.27215 13.4855 3.91891 15.1911C4.56566 16.8967 5.71539 18.3654 7.21574 19.4028C8.7161 20.4402 10.4963 20.9972 12.3203 21M3.93331 9H20.7333M3.93331 15H13.3333"
                stroke="#26303E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
              <path
                d="M11.8333 3C10.1487 5.69961 9.25552 8.81787 9.25552 12C9.25552 15.1821 10.1487 18.3004 11.8333 21M12.8333 3C14.7525 6.07385 15.6386 9.68077 15.3623 13.294M16.3333 22L21.3333 17M21.3333 17V21.5M21.3333 17H16.8333"
                stroke="#26303E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            </svg>

            <span class="ml-2">Website:</span>
          </p>
          <a :href="'http://' + user.website" class="text-blue-500 hover:underline block mb-4 font-extralight break-words"
            target="_blank">
            {{ user.website }}
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import service from "@/services/service";

export default {
  name: "UserCard",
  data() {
    return {
      users: [],
    };
  },
  async mounted() {
    await this.fetchUsersData();
  },

  methods: {
    async fetchUsersData() {
      try {
        const response = await service.get("/users/");
        if (Array.isArray(response.data.data)) {  // Ensure it's an array
          this.users = response.data.data;
        } else {
          console.error("Unexpected API response format:", response.data);
          this.users = [];  // Fallback to empty array
        }
      } catch (error) {
        console.error("Error fetching users:", error);
        this.users = [];  // Prevent Vue from crashing
      }
    }
    ,
  },
};
</script>

<style scoped></style>
