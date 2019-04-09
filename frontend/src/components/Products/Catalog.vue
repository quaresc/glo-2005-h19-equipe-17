<template>
  <section class="section columns is-fullheight" style="position: relative">
    <catalog-menu
      :perPage.sync="perPage"
      v-on:update:perPage="getProducts"
      :rating.sync="rating"
      v-on:update:rating="getProducts"
    />
    <div class="columns is-multiline" v-if="products">
      <catalog-detail
        v-for="(product, index) in products"
        :product="product"
        :key="index"
      ></catalog-detail>
      <div class="column is-three-fifths is-offset-one-fifth">
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
    <b-loading :is-full-page="false" :active.sync="isLoading"></b-loading>
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
      isLoading: false,
      currentPage: 1,
      perPage: 10,
      total: 0,
      rating: 0,
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
        perPage: this.perPage,
        rating: this.rating
      };
      try {
        this.isLoading = true;
        await HTTP.get(
          this.$route.params.department
            ? "/products/department/" + this.$route.params.department
            : "/products",
          { params }
        ).then(response => {
          this.products = response.data.products;
          this.total = response.data.total_products;
          this.isLoading = false;
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
