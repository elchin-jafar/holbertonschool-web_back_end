export default function getListStudentIds(array) {
  if (Array.isArray(array)) return array.map((obj) => obj.id);
  return [];
}
