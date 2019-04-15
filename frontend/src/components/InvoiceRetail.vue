<template>
  <div class="data-invoice container">
    <b-table :data="invoice" :columns="columns" v-if="invoice"></b-table>

    <div class="buttons">
      <router-link :to="{ name: 'Invoice' }">
        <button class="button is-secondary">
          <strong>List Invoices</strong>
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
import { HTTP } from "@/plugins/axios";

export default {
  name: "invoice",
  data() {
    return {
      invoice: null,
      columns: [
        {
          field: "name",
          label: "Product name",
        },
        {
          field: "price",
          label: "Price"
        },
        {
          field: "quantity",
          label: "Quantity"
        }
      ]
    };
  },
  created() {
          this.id = this.$route.params.id;
      },
  async mounted() {
    try {
      this.invoice = await HTTP.get("/users/invoice/"+ this.id).then(response => {
        return response.data;
      });
    } catch (error) {
      console.error(error);
    }
  }
};
</script>

<style scoped>
.data-invoice {
  margin-top:60px;
}
</style>
