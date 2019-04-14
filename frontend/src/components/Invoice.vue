<template>
  <b-table :data="invoice" :columns="columns" v-if="invoice"></b-table>
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
          label: "ID",
          width: "40",
          numeric: true
        },
        {
          field: "montant",
          label: "Somme total"
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
