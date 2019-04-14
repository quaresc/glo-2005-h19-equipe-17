<template> </template>

<script>
export default {
  data() {
    return {
      cart: {}
    };
  },
  async mounted() {
    await this.getCart();
  },
  methods: {
    async getCart() {
      return await HTTP.get(`/users/1/cart`).then(response => {
        return (this.cart = response.data);
      });
    }
  }
};
</script>

<style lang="sass" scoped>

</style>


