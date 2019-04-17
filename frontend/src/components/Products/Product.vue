<template>
  <section v-if="product" class="section">
    <div class="tile">
      <div class="tile is-5 is-parent is-vertical">
        <figure class="image is-square">
          <img :src="product.image_url" />
        </figure>
      </div>
      <div class="tile is-parent is-vertical">
        <div class="tile-content">
          <div class="media">
            <div class="media-content">
              <p class="title is-4">{{ product.name }}</p>
              <p class="subtitle is-4">
                {{ product.type }} - Seller: {{ product.company }}
              </p>
              <star-rating
                :rating="product.rating"
                read-only
                :show-rating="false"
                :star-size="20"
              />
              <br />
              <p class="title is-5">Description</p>
              <p class="subtitle is-6">{{ product.description }}</p>
              <p class="subtitle is-6">Weight: {{ product.weight }}kg</p>
            </div>
            <div class="media-right has-text-centered">
              <span class="tag is-secondary is-large is-rounded"
                >${{ product.price }}</span
              >
              <br />
              <br />
              <span
                class="tag is-primary is-medium is-rounded"
                v-if="product.quantity > 0 && product.quantity < 10"
                ><strong>{{ product.quantity }} remaining, hurry!</strong></span
              >
              <span class="tag is-primary is-medium is-rounded" v-else
                ><strong>{{ product.quantity }} remaining</strong></span
              >
            </div>
          </div>
          <br />
          <button
            class="button is-primary is-rounded is-fullwidth"
            :disabled="added === true || product.quantity === 0"
            @click="addToCart()"
          >
            Add to cart
          </button>
          <p
            v-if="product.quantity === 0"
            class="subtitle has-text-centered is-6"
          >
            This product is currently out of stock
          </p>
        </div>
      </div>
    </div>
    <review />
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
      added: false,
      defaultQuantity: 1
    };
  },
  async mounted() {
    await this.getProduct();
  },
  methods: {
    async getProduct() {
      let productId = this.$route.params.id;
      try {
        await HTTP.get("/products/" + productId)
          .then(response => {
            this.product = response.data.product;
          })
          .catch(error =>
            this.$toast.open({
              duration: 5000,
              message: error.response.data.message,
              position: "is-bottom",
              type: "is-danger"
            })
          );
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
              type: "is-success",
              position: "is-bottom"
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