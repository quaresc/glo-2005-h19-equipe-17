<template>
  <section v-if="product" class="section">
    <div class="tile">
      <div class="tile is-5 is-parent is-vertical">
        <figure class="image is-square">
          <img :src="product.image_url">
        </figure>
      </div>
      <div class="tile is-parent is-vertical">
        <div class="tile-content">
          <div class="media">
            <div class="media-content">
              <p class="title is-4">{{ product.name }}</p>
              <p class="subtitle is-4">{{ product.type }} - Seller: {{ product.company }}</p>
              <div class="subtitle is-6">{{ product.ean }}</div>
              <star-rating :rating="product.rating" read-only :show-rating="false" :star-size="20"/>
              <p class="subtitle is-6">Price: {{ product.price }}$</p>
              <p class="subtitle is-6">Weight: {{ product.weight }}kg</p>
              <p class="subtitle is-6">Description: {{ product.description }}</p>
            </div>
          </div>
          <br>
          <button class="button is-primary is-rounded is-fullwidth" @click="addToCart()">Add to cart</button>
        </div>
      </div>
    </div>
    <review/>
  </section>
</template>

<script lang="ts">
import { HTTP } from "@/plugins/axios";
import Review from "@/components/Reviews/Review.vue";

export default {
  components: {
    Review
  },
  data() {
    return {
      product: null,
      defaultQuantity: 1
    };
  },
  async mounted() {
    this.getProduct();
  },
  methods: {
    async getProduct() {
      let productId = this.$route.params.id;
      try {
        await HTTP.get("/products/" + productId).then(response => {
          this.product = response.data.product;
        });
      } catch (error) {
        console.error(error);
      }
    },
    async addToCart() {
      let productId = this.$route.params.id;
      let userId = 1; // TODO: Replace with a real variable
      const cart = {
        quantity: this.defaultQuantity
      };
      try {
        await HTTP.post("/users/" + userId + "/cart/" + productId, {
          cart
        }).then(response => {
          if (response.data === "Duplicate") {
            this.$toast.open({
              duration: 5000,
              message: "You already added this product to your cart.",
              position: "is-bottom",
              type: "is-danger"
            });
          } else {
            this.$toast.open({
              message: "You added this product to your cart!",
              type: "is-success"
            });
          }
        });
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>

<style lang="sass" scoped>
img
  object-fit: contain;
  cursor: pointer;
.is-fullheight
    height: 100%;
</style>