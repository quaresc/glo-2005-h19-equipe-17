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
          field: "id",
          label: "ID",
          width: "40",
          numeric: true
        },
        {
          field: "at",
          label: "date"
        }
      ]
    };
  },
  async mounted() {
    try {
      this.invoice = await HTTP.get("/users/1/invoices").then(response => {
        return response.data;
      });
    } catch (error) {
      console.error(error);
    }
  }
};
</script>
