<template>
  <b-table :data="invoice" :columns="columns" v-if="invoice"></b-table>
</template>

<script>
import { HTTP } from "@/plugins/axios";

export default {
  name: "Invoice",
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
          field: "firstName",
          label: "First Name"
        },
        {
          field: "lastName",
          label: "Last Name"
        },
        {
          field: "age",
          label: "Age",
          numeric: true
        }
      ]
    };
  },
  async mounted() {
    try {
      this.invoice = await HTTP.get("/users/10/invoice").then(response => {
        return response.data;
      });
    } catch (error) {
      console.error(error);
    }
  }
};
</script>
