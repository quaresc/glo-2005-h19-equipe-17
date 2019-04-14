import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home.vue";
import Invoice from "@/views/Invoice.vue";
import InvoiceRetail from "@/views/InvoiceRetail.vue";
import NotFound from "@/views/NotFound.vue";
import ProductView from "@/views/ProductView.vue";
import Catalog from "@/components/Products/Catalog.vue";
import Cart from "@/views/CartView.vue";

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
            path: "/products/:id",
            name: "Product",
            component: ProductView
        },
        {
            path: "/catalog/:department?",
            name: "Catalog",
            component: Catalog
        },
        {
            path: "/invoices",
            name: "Invoice",
            component: Invoice
        },
        {
            path: "/invoice/:id",
            name: "InvoiceRetail",
            component: InvoiceRetail
        },
        {
            path: "/cart",
            name: "Cart",
            component: Cart
        }
    ]
});
