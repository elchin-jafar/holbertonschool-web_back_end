/* eslint-disable */
export default function updateStudentGradeByCity(studs, city, newG) {
  const sts = studs.filter((ob) => ob.location === city);

  sts.map((ob) => {
    const grades = newG.find((obj) => obj.studentId === ob.id);
    if (grades) ob.grade = grades.grade;
    else ob.grade = 'N/A';
  });

  return sts;
}
