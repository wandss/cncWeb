export default class Form {

  constructor(metadata={}) {
    this.metadata = metadata;
  }
  getLabel(key){
    return this.metadata[key].label || '';
  }
  getMaxLength(key){
    return this.metadata[key]['max_length'];
  }
}
