<template>
  <section class="section is-centered columns">
    <div v-if="cart.length > 0" class="tile is-ancestor">
      <div class="tile is-parent is-vertical is-8">
        <article class="tile is-child notification">
          <p class="title">Shopping cart</p>
          <cart-list :cart="cart" />
        </article>
      </div>
      <div class="tile is-parent">
        <article class="tile is-child notification">
          <div class="content">
            <p class="title">Subtotal</p>
            <p class="subtitle">With even more content</p>
            <div class="content">
              <!-- Content -->
            </div>
          </div>
        </article>
      </div>
    </div>
    <div v-else class="columns section">
      <div class="column has-text-centered">
        <p class="title is-1">Your cart is currently empty !</p>
        <p class="subtitle is-3">
          Find some inspiration in our catalog
        </p>
        <router-link :to="{ name: 'Home' }">
          <a class="button is-primary is-large">Back to home</a>
        </router-link>
      </div>
    </div>
  </section>
</template>

<script>
import { HTTP } from "@/plugins/axios";
import CartList from "@/components/Cart/CartList.vue";

export default {
  data() {
    return {
      cart: []
    };
  },
  components: {
    CartList
  },
  async mounted() {
    await this.getCart();
  },
  methods: {
    async getCart() {
      return await HTTP.get(`/users/1/cart`).then(response => {
        return (this.cart = response.data.products);
      });
    }
  }
};
</script>

<style lang="sass" scoped>

</style>


