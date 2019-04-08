<template>
  <section v-if="products" class="section">
    <div class="columns is-multiline">
      <catalog-detail
        v-for="(product, index) in products"
        :product="product"
        :key="index"
      ></catalog-detail>
    </div>
    <b-pagination
      :total="total"
      :current.sync="currentPage"
      :per-page="perPage"
      order="is-centered"
      rounded
      v-on:update:current="getProducts"
    >
    </b-pagination>
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
      perPage: 5,
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
