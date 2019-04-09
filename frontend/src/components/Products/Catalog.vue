<template>
  <section v-if="products" class="section columns is-fullheight">
    <catalog-menu :perPage.sync="perPage" v-on:update:perPage="getProducts" />
    <div class="columns is-multiline">
      <catalog-detail
        v-for="(product, index) in products"
        :product="product"
        :key="index"
      ></catalog-detail>
      <div class="column">
        <b-pagination
          class="pagination"
          :total="total"
          :current.sync="currentPage"
          :per-page="perPage"
          rounded
          order="is-centered"
          v-on:update:current="getProducts"
        >
        </b-pagination>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { HTTP } from "@/plugins/axios";
import CatalogDetail from "@/components/Products/CatalogDetail.vue";
import CatalogMenu from "@/components/Products/CatalogMenu.vue";

export default {
  name: "Catalog",
  components: {
    CatalogMenu,
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
        window.scrollTo(0, 0);
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>

<style scoped>
.pagination {
  clear: both;
}
</style>
