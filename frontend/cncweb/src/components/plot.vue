<template>
  <modal :show="show" @click="$emit('click')"  modalSize="modal-full"
  title="Start your engines...">
    <div slot="body">
      <progress-bar v-bind="progress" />
      <upload label="Upload GCode File" name="upload"
       @change="handleUpload"
       />
      <i>{{gcode_file}}</i>
    </div>
    <div slot="footer" >
      <base-btn cssClass="btn btn-warning" :disabled="isDisabledBtn"
        @click="startPlotting">
        Start Plotting
      </base-btn>
    </div>
  </modal>
</template>
<script>
import BaseBtn from '@/components/baseButton.vue'
import Modal from '@/components/Modal.vue'
import Upload from '@/components/Upload.vue'
import ProgressBar from '@/components/Progressbar.vue'
import ProgressBarModel from '@/utils/progressbarModel.js'
export default {
  name: 'plot',
  components: {BaseBtn, Modal, Upload, ProgressBar},
  props: {
    show: {
      type: Boolean,
      default: false,
      required: true,
    }
  },
  data(){
    return {
      gcode_file: null,
      uploadedFileId: null,
      progress: new ProgressBarModel(),
      isDisabledBtn: true,
    }
  },
  methods: {
    handleUpload(ark){
      this.progress = new ProgressBarModel()
      this.progress.show = true
      const config = {
        onUploadProgress:((progressEvent)=>{
          let percentCompleted = Math.round((progressEvent.loaded *100)/
            progressEvent.total);
            this.progress.progress = percentCompleted
        }),
      }
      this.isDisabledBtn = false
      for(let i=0; i<ark.length; i++){
        this.gcode_file = ark[i].name
        this.$http.post(this.$urls.plot.upload+ark[i].name, ark[i], config)
          .then(resp=>{
            console.log(resp)
            console.log(resp.data)
            this.uploadedFileId = resp.data.id
            this.progress.show = false
          })
          .catch(error=>{
            console.log(error)
            console.log(error.response)
            this.progress.show = false
          })
      }
    },
    startPlotting(){
      this.progress = new ProgressBarModel()
      this.isDisabledBtn = true
      console.log('Stat Plotting.......')
      console.log('Open Loader')
    }
  }
}
</script>
