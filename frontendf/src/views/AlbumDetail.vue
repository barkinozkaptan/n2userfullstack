<template>
  <div class="pt-8">
    <div class="p-6">
      <GoBackButton
        routeName="Albums"
        :routeParams="{ id: userId }"
        buttonLabel="Go Albums"
      />

      <div v-if="albumPhotos.length > 0" class="flex flex-wrap justify-start gap-4 pt-4">
        <img
          v-for="(photo, index) in albumPhotos"
          :key="index"
          :src="photo.url"
          :alt="photo.title"
          class="w-56 h-56 object-cover rounded-lg shadow-md"
        />
      </div>
      <div v-else class="text-center text-gray-500">
        No photos found for this album.
      </div>
    </div>
  </div>
</template>

<script>
import GoBackButton from "@/components/GoBackButton.vue";
import service from "@/services/service";

export default {
  name: "AlbumDetails",
  components: {
    GoBackButton,
  },
  data() {
    return {
      albumPhotos: [],
    };
  },
  computed: {
    userId() {
      return this.$route.params.userId;
    },
    albumId() {
      return this.$route.params.albumId;
    },
  },
  mounted() {
    this.fetchPhotos(); // ✅ Now Vue will correctly find the function
  },
  methods: {
    async fetchPhotos() {
      try {
        const response = await service.get(`/photos/album/${this.albumId}/`);
        
        console.log("🔍 API Response:", response.data); // ✅ Debugging output

        if (response.data.source === "redis") {
          console.log("✅ Photos fetched from Redis cache:", response.data.data);
        } else {
          console.log("📌 Photos fetched from database:", response.data.data);
        }
        
        this.albumPhotos = Array.isArray(response.data.data) ? response.data.data : [];
      } catch (error) {
        console.error("❌ Error fetching photos:", error);
        this.albumPhotos = [];
      }
    }
  }
};
</script>
