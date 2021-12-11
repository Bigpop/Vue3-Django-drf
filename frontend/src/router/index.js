import { createWebHistory, createRouter } from "vue-router";
import Home from "@/views/Home.vue";
import Article from "@/views/Article.vue";
import Whisper from "@/views/Whisper.vue";
import TransForum from "@/views/TransForum.vue"
const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/article/:id",
        name: "Article",
        component: Article
    },
    {
        path: "/whisper",
        name: "Whisper",
        component: Whisper
    },
    {
        path: "/transforum",
        name: "TransForum",
        component: TransForum
    },
];

const router = createRouter({
    // https://next.router.vuejs.org/guide/essentials/history-mode.html
    history: createWebHistory(),
    routes,
});

export default router;