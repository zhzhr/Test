<template>
    
  <ExcelTable :data="data"></ExcelTable>
</template>

<script>
import { ExcelTable } from '../../node_modules/exceljs/excel';

export default {
    data: function() {
      return {
        data: []
      };
    },
    components: {
      ExcelTable
    }
}
</script>

<style scoped>


</style>