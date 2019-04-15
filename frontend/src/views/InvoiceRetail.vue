<template>
  <div class="invoice">
    <InvoiceRetail />
  </div>
</template>


<script>
import InvoiceRetail from "@/components/Invoice/InvoiceRetail.vue";

export default {
  name: "invoiceretail",
  components: {
    InvoiceRetail
  }
};
</script>
