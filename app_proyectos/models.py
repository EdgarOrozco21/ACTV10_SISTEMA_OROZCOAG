from django.db import models

# NOTA: Asumimos que Empleado y Campaña son modelos que existen.
# Si no existen, usa models.IntegerField para id_empleado e id_campaña.
# Para este ejemplo, usaremos IntegerField para simplificar.

class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_entrega = models.DateField()
    # Asumimos que son claves foráneas a otros modelos
    id_empleado = models.IntegerField()  # models.ForeignKey(Empleado, on_delete=models.CASCADE)
    id_campaña = models.IntegerField()  # models.ForeignKey(Campaña, on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre