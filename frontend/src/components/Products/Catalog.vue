<template>
  <section class="section columns is-fullheight" style="position: relative">
    <catalog-menu
      :perPage.sync="perPage"
      v-on:update:perPage="updateFilter"
      :rating.sync="rating"
      v-on:update:rating="updateFilter"
      :department="department"
    />
    <div v-if="products && products.length !== 0">
      <div class="columns is-centered is-multiline">
        <catalog-detail
          v-for="(product, index) in products"
          :product="product"
          :key="index"
        ></catalog-detail>
      </div>
      <div class="columns is-centered is-multiline">
        <div class="column is-half">
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
    </div>
    <div
      v-else-if="products && products.length === 0"
      class="column is-centered"
    >
      <div class="column has-text-centered">
        <p class="title is-1">
          We currently have no products for this department :(
        </p>
        <p class="subtitle is-3">
          Please come back in a few days !
        </p>
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
      isLoading: false,
      currentPage: 1,
      perPage: 10,
      total: 0,
      rating: 0,
      products: null
    };
  },
  computed: {
    department() {
      if (this.$route.query.search) {
        return `Results for '${this.$route.query.search}'`;
      }
      return this.$route.params.department
        ? this.$route.params.department
        : "All products";
    }
  },
  async mounted() {
    await this.getProducts();
  },
  methods: {
    updateFilter() {
      this.currentPage = 1;
      this.getProducts();
    },
    async getProducts() {
      const params = {
        page: this.currentPage,
        perPage: this.perPage,
        rating: this.rating
      };
      if (this.$route.query.search) {
        Object.assign(params, { search: this.$route.query.search });
      }
      try {
        this.isLoading = true;
        await HTTP.get(
          this.$route.params.department
            ? "/products/department/" + this.$route.params.department
            : "/products",
          { params }
        )
          .then(response => {
            this.products = response.data.products;
            this.total = response.data.total_products;
            this.isLoading = false;
          })
          .catch(error =>
            this.$toast.open({
              duration: 5000,
              message: error.response.data.message,
              position: "is-bottom",
              type: "is-danger"
            })
          );
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
