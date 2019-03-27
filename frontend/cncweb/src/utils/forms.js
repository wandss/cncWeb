export default class Form {
  constructor(metadata, formData) {
    this.metadata = metadata;
    this.formData = formData;
    this.data = [];
  }
  fillForm(){
    Object.keys(this.metadata).forEach(fieldName=>{
      this.formData.forEach(data=>{
        let meta = this.metadata[fieldName]
        meta['value'] = data[fieldName]
        this.data.push({[fieldName]: meta})
      })
    })
  }
}
/*TODO: Creates a method to update data to force the rerendering of component?
 * at this point in order to force a rerendering at vue component, is required to
 * update field values by using $set, as explained in documentation*/
