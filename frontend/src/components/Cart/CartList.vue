<template>
  <section class="cart-list">
    <div class="card" v-for="(product, index) in cart" :key="product.id">
      <div class="card-content">
        <div class="media">
          <div class="media-left">
            <figure class="image is-48x48">
              <img :src="product.image_url" />
            </figure>
          </div>
          <div class="media-content">
            <div class="columns is-vcentered">
              <div class="column is-three-fifths">
                <p class="title is-6">{{ product.name }}</p>
                <p class="subtitle is-6">{{ product.company }}</p>
                <star-rating
                  :rating="product.rating"
                  read-only
                  :show-rating="false"
                  :star-size="17"
                />
              </div>
              <div class="column has-text-centered">
                <p class="subtitle is-6 has-text-weight-semibold">
                  ${{ product.price }}
                </p>
              </div>
              <b-select
                placeholder="Quantity"
                v-model="quantity[index]"
                @input="updateQuantity(product.id, quantity[index])"
              >
                <option v-for="index in 10" :value="index" :key="index">{{
                  index
                }}</option>
              </b-select>
              <button
                class="button is-secondary"
                @click="deleteFromCart(product.id)"
              >
                <b-icon icon="trash-alt" size="is-small"></b-icon>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { HTTP } from "@/plugins/axios";

export default {
  props: {
    cart: Array,
    updateQuantity: Function
  },
  data() {
    return {
      quantity: []
    };
  },
  mounted() {
    this.cart.forEach(product => {
      this.quantity.push(product.quantity);
    });
  },
  methods: {
    async deleteFromCart(productId) {
      await HTTP.delete("/users/1/cart/" + productId, {}).then(async () => {
        this.$router.go();
      });
    }
  }
};
</script>

<style scoped>
.cart-list {
  max-height: 67vh;
  overflow-y: scroll;
}
</style>


