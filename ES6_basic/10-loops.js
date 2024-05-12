export default function appendToEachArrayValue(array, appendString) {
  const result = [];
  for (const elememt of array) {
    result.push(appendString + elememt);
  }

  return array;
}
