<template>
  <div class="pt-8">
    <div v-if="albums.length === 0" class="text-center text-gray-500">
    </div>
    <div class="p-6">
      <GoBackButton
        routeName="Home"
        buttonLabel="Go to Home"
      />
      <div
        class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-6 pt-4"
      >
        <!-- Router link for each album -->
        <router-link
          v-for="album in albums"
          :key="album.id"
          :to="{ name: 'AlbumDetail', params: { userId: userId, albumId: album.id } }"
          class="bg-white border border-gray-300 rounded-lg shadow-lg p-6 flex flex-col h-96 transform transition-transform duration-300 hover:scale-105"
        >
          <div class="grid grid-cols-2 gap-2 mb-4">
            <img
              v-for="index in 4"
              :key="index"
              :src="`https://picsum.photos/seed/album${album.id}_${index}/200/200`"
              :alt="`Preview ${index}`"
              class="w-full h-32 object-cover rounded"
            />
          </div>
          <div class="flex items-center mb-6">
            <div class="ml-3">
              <h3 class="text-lg font-semibold text-gray-800">{{ album.title }}</h3>
            </div>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import GoBackButton from "@/components/GoBackButton.vue";
import service from "@/services/service";

export default {
  name: "Albums",
  props: {
    id: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      albums: [],
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
    this.fetchAlbums();
  },
  methods: {
    async fetchAlbums() {
    try {
        const response = await service.get(`/albums/user/${this.userId}/`);
        
        console.log("🔍 API Response:", response.data); // ✅ Debugging output

        if (response.data.source === "redis") {
            console.log("✅ Albums fetched from Redis cache:", response.data.data);
        } else {
            console.log("📌 Albums fetched from database:", response.data.data);
        }
        
        this.albums = Array.isArray(response.data.data) ? response.data.data : [];
    } catch (error) {
        console.error("❌ Error fetching albums:", error);
        this.albums = [];
    }
}
,
  },
};
</script>
