import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const result = [];
  result.push(new ClassRoom(19));
  result.push(new ClassRoom(20));
  result.push(new ClassRoom(34));
  return result;
}
