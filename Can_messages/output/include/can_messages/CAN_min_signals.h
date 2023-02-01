#ifndef HEADER_MIN_SIGNALS_H#define HEADER_MIN_SIGNALS_H
class CAN_min_signals {    public:        CAN_min_signals();	/*
	 get_the ambient temperature
	 */
	std:: string get_temperature();
	 	/*
	set the ambient temperature
	 */
	std::string set_temperature(float newValue);	/*
	 get_the ambient humidity percentage
	 */
	std:: string get_humidity();
	 	/*
	set the ambient humidity percentage
	 */
	std::string set_humidity(uint8_t newValue);
	private:
	 unint8_t m_startMsgID;	 unint8_t m_temperatureGetMsgID;	 unint8_t m_temperatureSetMsgID;	 unint8_t m_humidityGetMsgID;	 unint8_t m_humiditySetMsgID;};#endif //HEADER_MIN_SIGNALS_H