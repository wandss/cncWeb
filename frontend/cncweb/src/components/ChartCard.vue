<template>
  <card header="Totals" @close="totalPannel=false" :show="totalPannel"
    cssClass="info" :hasCloseBtn="true">
    <div slot="content">
      <grid :gridData="summary" />
    </div>
  </card>
</template>
<script>
import Cart from '@/components/card.vue'
export default{
  name:'ChartCard',
}
</script>
