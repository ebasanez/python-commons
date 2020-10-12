import startup_test
from alerts import AlertManager

alerts = AlertManager(startup_test.configuration)

alerts.sendAlert('Alert body')