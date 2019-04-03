<template>
  <b-table :data="users" :columns="columns" v-if="users"></b-table>
</template>

<script>
import { HTTP } from "@/plugins/axios";

export default {
  name: "Users",
  data() {
    return {
      users: null,
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
      this.users = await HTTP.get("/users").then(response => {
        return response.data;
      });
    } catch (error) {
      console.error(error);
    }
  }
};
</script>

<style scoped></style>
