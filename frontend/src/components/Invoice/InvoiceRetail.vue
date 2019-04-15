<template>
  <div class="data-invoice container">
    <p class="title-10">Retail for invoice #{{ id }}</p>
    <b-table :data="invoice" :columns="columns" v-if="invoice"></b-table>

    <div class="buttons margin-top">
      <router-link :to="{ name: 'Invoices' }">
        <button class="button is-secondary">
          <strong>Return to invoices list</strong>
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
          label: "Product name"
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
      this.invoice = await HTTP.get("/users/invoice/" + this.id).then(
        response => {
          return response.data;
        }
      );
    } catch (error) {
      console.error(error);
    }
  }
};
</script>

<style scoped>
.title-10 {
  margin-bottom: 20px;
}

.data-invoice {
  margin-top: 60px;
  background-color: #f5f5f5;
  padding: 20px;
}

.margin-top {
  margin-top: 20px;
}
</style>
