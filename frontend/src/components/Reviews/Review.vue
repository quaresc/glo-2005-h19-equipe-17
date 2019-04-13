<template>
  <section class="section">
    <div class="tile">
      <p class="title is-4">Reviews</p>
    </div>
    <add-review />
    <div id="reviews" class="columns is-multiline" v-if="reviews">
      <review-detail
        v-for="(review, index) in reviews"
        :review="review"
        :key="index"
      ></review-detail>
      <div class="column is-three-fifths is-offset-one-fifth">
        <b-pagination
          class="pagination"
          :total="total"
          :current.sync="currentPage"
          :per-page="perPage"
          rounded
          order="is-centered"
          v-on:update:current="getReviews"
        >
        </b-pagination>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { HTTP } from "@/plugins/axios";
import ReviewDetail from "@/components/Reviews/ReviewDetail.vue";
import AddReview from "@/components/Reviews/AddReview.vue";

export default {
  name: "Reviews",
  components: {
    ReviewDetail,
    AddReview
  },
  data() {
    return {
      isLoading: false,
      currentPage: 1,
      perPage: 3,
      total: 0,
      reviews: null
    };
  },
  async mounted() {
    this.getReviews();
  },
  methods: {
    async getReviews() {
      const params = {
        page: this.currentPage,
        perPage: this.perPage
      };
      let productId = this.$route.params.id;
      try {
        await HTTP.get("/products/" + productId + "/reviews", { params }).then(
          response => {
            this.reviews = response.data.product_reviews;
            this.total = response.data.total_product_reviews;
            this.isLoading = false;
          }
        );
        document.getElementById("reviews").scrollIntoView();
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>
