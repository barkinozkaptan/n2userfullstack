import { createRouter, createWebHistory } from "vue-router";
import UserTodos from "../views/UserTodos.vue";
import UserCard from "../components/UserCard.vue";
import Albums from "../views/Albums.vue";
import AlbumDetail from "../views/AlbumDetail.vue";
import Posts from "../views/Posts.vue";
import HomePage from "../views/HomePage.vue";
const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
  {
    path: "/user/:id/todos",
    name: "UserTodos",
    component: UserTodos,
    props: route => ({ id: Number(route.params.id) }) // Convert id to Number
  },
  {
    path: "/user/:id/posts",
    name: "Posts",
    component: Posts,
    props: true,
  },
  {
    path: "/user/:id/albums",
    name: "Albums",
    component: Albums,
    props: true,
  },
  {
    path: "/user/:userId/albums/:albumId",
    name: "AlbumDetail",
    component: AlbumDetail,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
