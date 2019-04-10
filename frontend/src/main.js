import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Buefy from "buefy";
import StarRating from "vue-star-rating";

Vue.use(Buefy, { defaultIconPack: "fa" });
Vue.component("star-rating", StarRating);

Vue.config.productionTip = false;

new Vue({
    router,
    render: (h) => h(App)
}).$mount("#app");
