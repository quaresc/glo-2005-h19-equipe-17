<template>
  <section v-if="products" class="main-content columns is-fullheight">
    <aside
      class="menu is-2 is-narrow-mobile is-fullheight section is-hidden-mobile"
    >
      <p class="menu-label">
        Filter
      </p>
      <ul class="menu-list">
        <li><a>Dashboard</a></li>
        <li><a>Customers</a></li>
      </ul>
      <p class="menu-label">
        Administration
      </p>
      <ul class="menu-list">
        <li><a>Invitations</a></li>
        <li><a>Cloud Storage Environment Settings</a></li>
        <li><a>Authentication</a></li>
      </ul>

      <b-pagination
        :total="total"
        :current.sync="currentPage"
        :per-page="perPage"
        rounded
        simple
        v-on:update:current="getProducts"
      >
      </b-pagination>
    </aside>
    <div class="columns is-multiline">
      <catalog-detail
        v-for="(product, index) in products"
        :product="product"
        :key="index"
      ></catalog-detail>
    </div>
  </section>
</template>

<script lang="ts">
import { HTTP } from "@/plugins/axios";
import CatalogDetail from "@/components/Products/CatalogDetail.vue";

export default {
  name: "Catalog",
  components: {
    CatalogDetail
  },
  data() {
    return {
      currentPage: 1,
      perPage: 10,
      total: 0,
      products: null
    };
  },
  async mounted() {
    this.getProducts();
  },
  methods: {
    async getProducts() {
      const params = {
        page: this.currentPage,
        perPage: this.perPage
      };
      try {
        await HTTP.get("/products", { params }).then(response => {
          this.products = response.data.products;
          this.total = response.data.total_products;
        });
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>

<style scoped></style>
