<template>
  <section class="section is-centered columns">
    <div v-if="cart.length > 0" class="tile is-ancestor">
      <div class="tile is-parent is-vertical is-8">
        <article class="tile is-child notification">
          <p class="title">Shopping cart</p>
          <cart-list :cart="cart" :updateQuantity="updateQuantity"/>
          <br>
          <button class="button is-secondary" @click="deleteCart()">Delete cart</button>
        </article>
      </div>
      <div class="tile is-parent">
        <article class="tile is-child notification">
          <div class="content">
            <p class="title">Subtotal</p>
            <div class="content">
              <p class="subtitle is-3">${{ total }}</p>
            </div>
          </div>
          <button class="button is-primary" @click="submitPurchase()">Confirm purchase</button>
        </article>
      </div>
    </div>
    <div v-else class="columns section">
      <div class="column has-text-centered">
        <p class="title is-1">Your cart is currently empty !</p>
        <p class="subtitle is-3">Find some inspiration in our catalog</p>
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
  computed: {
    total() {
      let total = 0;
      this.cart.forEach(element => {
        total += element.price * element.quantity;
      });
      return Number.parseFloat(total).toFixed(2);
    }
  },
  async mounted() {
    await this.getCart();
  },
  methods: {
    async getCart() {
      return await HTTP.get(`/users/1/cart`).then(response => {
        return (this.cart = response.data.products);
      });
    },
    async updateQuantity(productId, quantity) {
      await HTTP.patch(`/users/1/cart/${productId}`, {
        quantity: quantity
      }).then(async () => {
        return await this.getCart();
      });
    },
    async deleteCart() {
      await HTTP.delete("/users/1/cart").then(async () => {
        this.$router.go();
      });
    },
    async submitPurchase() {
      let products = [];
      this.cart.forEach(element => {
        let product = {
          productId: element.id,
          quantity: element.quantity
        };
        products.push({ product });
      });
      await HTTP.post("/users/1/purchase", { products }).then(async () => {
        this.$router.push({
          name: "Invoices"
        });
        this.$toast.open({
          duration: 5000,
          message: "Thank you for your purchase !",
          position: "is-bottom",
          type: "is-success"
        });
      });
    }
  }
};
</script>

<style scoped>
html {
  height: 100%;
}
</style>


