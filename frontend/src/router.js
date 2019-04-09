import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home.vue";
import NotFound from "@/views/NotFound.vue";
import Catalog from "@/components/Products/Catalog.vue";

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: "/",
            name: "Home",
            component: Home
        },
        {
            path: "*",
            name: "404",
            component: NotFound
        },
        {
            path: "/catalog/:department?",
            name: "catalog",
            component: Catalog
        }
    ]
});
