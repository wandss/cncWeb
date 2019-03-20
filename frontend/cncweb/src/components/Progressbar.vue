<template>
  <div style="position:absolute">
    <overlay :show="show">
      <div class="container">
        <div class="progress">
          <div class="progress-bar progress-bar-animated progress-bar-striped"
           role="progressbar" :aria-valuenow="progress" aria-valuemin="0"
           aria-valuemax="100" :style="{width: progress.toString()+'%'}"
            >
            <span v-if="showCounter">
              {{progress}}%
            </span>
          </div>
        </div>
      </div>
    </overlay>
  </div>
</template>
<script>
import Overlay from '@/components/Overlay';
export default {
  name:'ProgressBar',
  components: {Overlay},
  props: {
    show:{
      type: Boolean,
      default: false,
    },
    progress: {
      type: [Number, String],
      default: 10,
    },
    showCounter: {
      type: Boolean,
      default: true,
    }
  }
}
</script>
<style scope>
.container{
  margin-top:35vh;
}
.progress{
  height:1.3rem;
}
</style>
