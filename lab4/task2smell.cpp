// 2.	Рефакторинг на рівні окремих операторів
int getSpeed() 
{
  int result = 0;

  if (isTransport()) 
  {
    if(isCar)  
    {
        result = getCarSpeed();
    } 
    // непотрібні вкладені умови
    else 
    {
      if(isPlane) { 
        for (int i = 0; i < m_planes.Length; i++) {
          result += getPlaneSpeed(m_planes[i]);
        }
        // непотрібна умова
        // якщо масив пустий, то цикл не запуститься 
        if (m_planes.Length > 0) {
          result = result / m_planes.Length;
        }
      }
      // непотрібні вкладені умови
      else {
        if(isBoat) {
          result = getBoatSpeed();
        }
      }
    }
  }
  else {
    result = getManSpeed();
  }
  return result;
}

