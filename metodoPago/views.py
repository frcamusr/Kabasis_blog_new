from django.utils import timezone
import pytz
from django.http import JsonResponse
from django.shortcuts import render
import mercadopago
from .models import PlanPago, datosComprador
from .models import RegistroTransaccion
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render


from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
import pytz

def payment_success(request):
    # Obtenemos los parámetros de la URL
    registro_id = request.GET.get('registro_id')
    payment_id = request.GET.get('payment_id')



    # Si no existe, continuamos con la lógica normal
    status = request.GET.get('status')
    payment_type = request.GET.get('payment_type')
    merchant_order_id = request.GET.get('merchant_order_id')

    # Obtiene la fecha y hora actual en la zona horaria de Chile (UTC-3)
    chile_tz = pytz.timezone('America/Santiago')
    current_datetime = timezone.now().astimezone(chile_tz)

    # Formatea la fecha y la hora por separado
    transaction_date = current_datetime.strftime("%Y-%m-%d")
    transaction_time = current_datetime.strftime("%H:%M:%S")

    # Obtén el plan de pago y el usuario correspondientes
    usuario = request.user

    if not RegistroTransaccion.objects.filter(payment_id=payment_id).exists():
    # Crea y guarda la transacción en la base de datos
        registro_transaccion = RegistroTransaccion.objects.create(
            payment_id=payment_id,
            status=status,
            payment_type=payment_type,
            merchant_order_id=merchant_order_id,
            fecha_transaccion=transaction_date,
            hora_transaccion=transaction_time,
            id_plan_id=registro_id,
            usuario=usuario,
        )
    # Recupera el registro de la base de datos a partir del payment_id
    registro_recuperado = get_object_or_404(RegistroTransaccion, payment_id=payment_id)
    # Puedes pasar el registro_recuperado al contexto para enviarlo al frontend
    context = {
        'registro_recuperado': registro_recuperado,
    }
    return render(request, 'aprobado.html', context)





def payment_failure(request):
    return render(request, 'fallo.html')


from django.shortcuts import render
from .models import PlanPago, Zona


from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def servicios(request):
    if request.method == 'POST':

        request.session['nombre_completo'] = request.POST.get('nombre', '')
        request.session['correo'] = request.POST.get('correo', '')


        # Redirige a la vista metodoPago
        return redirect('metodopago')

    # Si es una solicitud GET, continúa normalmente
    servicios_disponibles = PlanPago.objects.all()
    regiones = Zona.objects.values_list('region', flat=True).distinct()

    comunas_por_region = {}
    for region in regiones:
        comunas = Zona.objects.filter(region=region).values_list('comuna', flat=True).distinct()
        comunas_por_region[region] = list(comunas)

    nombre_completo = f"{request.user.first_name} {request.user.last_name}"
    correo = request.user.email
    # Pasa los servicios, regiones y comunas al contexto del template
    context = {
        'servicios_disponibles': servicios_disponibles,
        'regiones': regiones,
        'comunas_por_region': comunas_por_region,
        'nombre_completo': nombre_completo,
        'correo': correo,
    }

    # Renderiza la plantilla con el contexto
    return render(request, 'serviciosDisponibles.html', context)




def selmetodopago(request):
    sdk = mercadopago.SDK("TEST-6880120315254295-121514-a2d137b6af8a7d9b4b869e89ef7713d3-763149216")
    preference_data = {}
    context = {}


    if request.method == 'POST':
        # Obtener datos del formulario enviado por el frontend
        plan_id = request.POST.get('plan_id')
        correo_comprador = request.POST.get('correo', '')
        plan_seleccionado = PlanPago.objects.get(id=plan_id)

        # Intenta encontrar un registro existente para el correo del comprador
        datos_comprador, created = datosComprador.objects.get_or_create(
            correoComprador=correo_comprador,
            defaults={'id_plan': plan_seleccionado}  # Esto se usa solo si se necesita crear
        )

        # Actualiza el registro con los nuevos datos recibidos del POST
        # Esta operación se hace independientemente de si el registro fue creado o no
        datos_comprador.id_plan = plan_seleccionado
        datos_comprador.tipoDocumento = request.POST.get('tipo_documento', '')
        datos_comprador.rutEmpresa = request.POST.get('rut_empresa', '')
        datos_comprador.razonSocial = request.POST.get('razon_social', '')
        datos_comprador.giro = request.POST.get('giro', '')
        datos_comprador.DireccionTributaria = request.POST.get('direccion_tributaria', '')
        datos_comprador.region = request.POST.get('region', '')
        datos_comprador.comuna = request.POST.get('comuna', '')
        datos_comprador.nombreComprador = request.POST.get('nombre', '')
        datos_comprador.rutComprador = request.POST.get('rut', '')
        # El correoComprador ya está establecido, por lo que no necesitamos actualizarlo aquí
        datos_comprador.numeroContacto = request.POST.get('telefono', '')
        datos_comprador.estadoPago = False  # Siempre reinicia este valor
        datos_comprador.save()


        preference_data["items"] = [plan_seleccionado.to_json()]
        preference_data["statement_descriptor"] = "KABASIS"
        preference_data['back_urls'] = {
            'success': request.build_absolute_uri(f'/metodoPago/success/?registro_id={plan_id}'),
            'failure': request.build_absolute_uri('/metodoPago/failure/')
        }

        preference_data['auto_return'] = 'approved'
        preference_data['binary_mode'] = True

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response['response']



        # Añadir los datos al contexto
        #context['plan_id'] = plan_id
        #context['tipo_documento'] = tipo_documento
        context.update({'preference': preference})

        # Redirigir a la página metodoPago.html con los datos

    # Si la solicitud no es POST, simplemente renderiza la página actual
    return render(request, 'metodoPago.html', context)





from django.shortcuts import redirect

def crearEmpresapago(request):
    return redirect('registro_empresa')


from django.shortcuts import render, get_object_or_404
from .models import datosComprador  # Asegúrate de tener importado el modelo correcto

def OrdenDeCompra(request):
    # Supongamos que puedes identificar al usuario/comprador por su correo o algún otro método
    correo_comprador = request.user.email  # Ejemplo si estás usando el correo del usuario autenticado
    
    # Obtén los datos del comprador; usa get_object_or_404 para manejar casos donde no se encuentre el objeto
    datos_comprador = get_object_or_404(datosComprador, correoComprador=correo_comprador)
    
    # No es necesario buscar el plan de pago por separado, ya que está asociado a datos_comprador
    plan_seleccionado = datos_comprador.id_plan
    
    # Prepara el contexto con los datos a pasar al template
    context = {
        'datos_comprador': datos_comprador,
        'plan_seleccionado': plan_seleccionado
    }
    
    # Renderiza el template con el contexto
    return render(request, 'OrdenDeCompra.html', context)

from django.shortcuts import render
from .models import datosComprador

def GenerarOrdenDeCompra(request):
    try:
        # Suponiendo que identificas al comprador por su usuario (ajusta según tu modelo)
        datos_del_comprador = datosComprador.objects.get(correoComprador=request.user.email)
    except datosComprador.DoesNotExist:
        datos_del_comprador = None

    return render(request, 'GenerarOrdenDeCompra.html', {'datos_del_comprador': datos_del_comprador})

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import datosComprador

def generarPDF(request):
    # Crea la respuesta HTTP con el contenido apropiado para un PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="orden_de_compra.pdf"'

    # Crea un objeto Canvas de ReportLab para dibujar el PDF
    p = canvas.Canvas(response)

    try:
        # Supongamos que obtenemos los datos del comprador por su usuario
        datos = datosComprador.objects.get(correoComprador=request.user.email)
        y = 800  # Coordenada Y inicial para el texto

        # Escribe los datos en el PDF
        p.drawString(100, y, f"ID: {datos.id}")
        p.drawString(100, y-20, f"Tipo Documento de Compra: {datos.tipoDocumento}")
        p.drawString(100, y-40, f"Rut Empresa: {datos.rutEmpresa}")
        p.drawString(100, y-60, f"Razón Social: {datos.razonSocial}")
        p.drawString(100, y-80, f"Giro Empresa: {datos.giro}")
        p.drawString(100, y-100, f"Dirección tributaria: {datos.DireccionTributaria}")
        p.drawString(100, y-120, f"Región : {datos.region}")
        p.drawString(100, y-140, f"Comuna: {datos.comuna}")
        p.drawString(100, y-160, f"Nombre Comprador: {datos.nombreComprador}")
        p.drawString(100, y-180, f"Rut del Comprador: {datos.rutComprador}")
        p.drawString(100, y-200, f"Correo del Comprador: {datos.correoComprador}")
        p.drawString(100, y-220, f"Numero de Contacto: {datos.numeroContacto}")
        p.drawString(100, y-240, f"Descripción Servicio: {datos.id_plan.description}")
        p.drawString(100, y-260, f"Precio Unitario: {datos.id_plan.unit_price}")
        # Continúa escribiendo más datos según necesites

    except datosComprador.DoesNotExist:
        p.drawString(100, 800, "Datos del comprador no encontrados.")

    # Finaliza el PDF y lo retorna en la respuesta
    p.showPage()
    p.save()
    return response

