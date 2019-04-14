<template>
  <div class="data-invoice container">
    <b-table :data="invoice" :columns="columns" v-if="invoice"></b-table>
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
          field: "id_invoice",
          label: "ID invoice",
        },
        {
          field: "montant",
          label: "Somme total (euros)"
        },
        {
          field: "transaction_date",
          label: "Date"
        }
      ]
    };
  },
  created() {
          this.id = this.$route.params.id;
      },
  async mounted() {
    try {
      this.invoice = await HTTP.get("/users/"+ this.id + "/invoices").then(response => {
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
  margin-top:80px;
}
</style>
