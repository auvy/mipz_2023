// 2.	Рефакторинг на рівні окремих операторів
int getSpeed() 
{
  int result = 0;

  if (!isTransport()) 
  {
    result = getManSpeed();
  }
  else if(isCar)  
  {
    result = getCarSpeed();
  } 
  else if(isBoat)
  {
    result = getBoatSpeed();
  }
  else if(isPlane)
  {
    for (int i = 0; i < m_planes.Length; i++) {
      result += getPlaneSpeed(m_planes[i]) / m_planes.Length;
    }
  }
  return result;
}

