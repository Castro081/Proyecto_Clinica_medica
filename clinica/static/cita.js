let dataTable;
let dataTableIsInitialized = false;


const dataTableOptions = {
    lengthMenu: [1, 3, 5],
    dom: 'Bfrtilp',
    buttons: [
        {
            extend: 'excelHtml5',
            text: '<i class="fas fa-file-excel"></i> ',
            titleAttr: 'Exportar a Excel',
            className: 'btn btn-success',
        },
        {
            extend: 'pdfHtml5',
            text: '<i class="fas fa-file-pdf"></i> ',
            titleAttr: 'Exportar a PDF',
            className: 'btn btn-danger',
        },
        {
            extend: 'print',
            text: '<i class="fa fa-print"></i> ',
            titleAttr: 'Imprimir',
            className: 'btn btn-info',
        },
    ],

    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7, 8,] },
        { orderable: false, targets: [0,1, 2,3, 6, 7, 8] },
        { searchable: false, targets: [0, 6, 7, 8] }
    ],
    pageLength: 4,
    destroy: true,
    language: {
        processing: 'Procesando...',
        lengthMenu: 'Mostrar _MENU_ registros',
        zeroRecords: 'No se encontraron resultados',
        emptyTable: 'Ningún dato disponible en esta tabla',
        infoEmpty: 'Mostrando registros del 0 al 0 de un total de 0 registros',
        infoFiltered: '(filtrado de un total de _MAX_ registros)',
        search: 'Buscar:',
        infoThousands: ',',
        loadingRecords: 'Cargando...',
        paginate: {
            first: 'Primero',
            last: 'Último',
            next: 'Siguiente',
            previous: 'Anterior',
        },
        aria: {
            sortAscending: ': Activar para ordenar la columna de manera ascendente',
            sortDescending: ': Activar para ordenar la columna de manera descendente',
        },
        buttons: {
            copy: 'Copiar',
            colvis: 'Visibilidad',
            collection: 'Colección',
            colvisRestore: 'Restaurar visibilidad',
            copyKeys:
            'Presione ctrl o u2318 + C para copiar los datos de la tabla al portapapeles del sistema. <br /> <br /> Para cancelar, haga clic en este mensaje o presione escape.',
        copySuccess: {
            1: 'Copiada 1 fila al portapapeles',
            _: 'Copiadas %ds fila al portapapeles',
        },
        copyTitle: 'Copiar al portapapeles',
        csv: 'CSV',
        excel: 'Excel',
        pageLength: {
            '-1': 'Mostrar todas las filas',
            _: 'Mostrar %d filas',
        },
        pdf: 'PDF',
        print: 'Imprimir',
        renameState: 'Cambiar nombre',
        updateState: 'Actualizar',
        createState: 'Crear Estado',
        removeAllStates: 'Remover Estados',
        removeState: 'Remover',
        savedStates: 'Estados Guardados',
        stateRestore: 'Estado %d',
        },
        autoFill: {
            cancel: 'Cancelar',
            fill: 'Rellene todas las celdas con <i>%d</i>',
            fillHorizontal: 'Rellenar celdas horizontalmente',
            fillVertical: 'Rellenar celdas verticalmentemente',
        },
        decimal: ',',
        searchBuilder: {
            add: 'Añadir condición',
            button: {
            0: 'Constructor de búsqueda',
            _: 'Constructor de búsqueda (%d)',
        },
        clearAll: 'Borrar todo',
        condition: 'Condición',
        conditions: {
            date: {
                after: 'Despues',
                before: 'Antes',
                between: 'Entre',
                empty: 'Vacío',
                equals: 'Igual a',
                notBetween: 'No entre',
                notEmpty: 'No Vacio',
                not: 'Diferente de',
            },
            number: {
                between: 'Entre',
                empty: 'Vacio',
                equals: 'Igual a',
                gt: 'Mayor a',
                gte: 'Mayor o igual a',
                lt: 'Menor que',
                lte: 'Menor o igual que',
                notBetween: 'No entre',
                notEmpty: 'No vacío',
                not: 'Diferente de',
            },
            string: {
                contains: 'Contiene',
                empty: 'Vacío',
                endsWith: 'Termina en',
                equals: 'Igual a',
                notEmpty: 'No Vacio',
                startsWith: 'Empieza con',
                not: 'Diferente de',
                notContains: 'No Contiene',
                notStartsWith: 'No empieza con',
                notEndsWith: 'No termina con',
            },
            array: {
                not: 'Diferente de',
                equals: 'Igual',
                empty: 'Vacío',
                contains: 'Contiene',
                notEmpty: 'No Vacío',
                without: 'Sin',
            },
        },
        data: 'Data',
        deleteTitle: 'Eliminar regla de filtrado',
        leftTitle: 'Criterios anulados',
        logicAnd: 'Y',
        logicOr: 'O',
        rightTitle: 'Criterios de sangría',
        title: {
            0: 'Constructor de búsqueda',
            _: 'Constructor de búsqueda (%d)',
        },
        value: 'Valor',
        },
        searchPanes: {
        clearMessage: 'Borrar todo',
        collapse: {
            0: 'Paneles de búsqueda',
            _: 'Paneles de búsqueda (%d)',
        },
        count: '{total}',
        countFiltered: '{shown} ({total})',
        emptyPanes: 'Sin paneles de búsqueda',
        loadMessage: 'Cargando paneles de búsqueda',
        title: 'Filtros Activos - %d',
        showMessage: 'Mostrar Todo',
        collapseMessage: 'Colapsar Todo',
        },
        select: {
            cells: {
                1: '1 celda seleccionada',
                _: '%d celdas seleccionadas',
        },
        columns: {
            1: '1 columna seleccionada',
            _: '%d columnas seleccionadas',
        },
        rows: {
            1: '1 fila seleccionada',
            _: '%d filas seleccionadas',
        },
        },
        thousands: '.',
        datetime: {
            previous: 'Anterior',
            next: 'Proximo',
            hours: 'Horas',
            minutes: 'Minutos',
            seconds: 'Segundos',
            unknown: '-',
            amPm: ['AM', 'PM'],
            months: {
            0: 'Enero',
            1: 'Febrero',
            10: 'Noviembre',
            11: 'Diciembre',
            2: 'Marzo',
            3: 'Abril',
            4: 'Mayo',
            5: 'Junio',
            6: 'Julio',
            7: 'Agosto',
            8: 'Septiembre',
            9: 'Octubre',
        },
        weekdays: ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab'],
        },
        editor: {
            close: 'Cerrar',
            create: {
                button: 'Nuevo',
            title: 'Crear Nuevo Registro',
            submit: 'Crear',
        },
        edit: {
            button: 'Editar',
            title: 'Editar Registro',
            submit: 'Actualizar',
        },
        remove: {
            button: 'Eliminar',
            title: 'Eliminar Registro',
            submit: 'Eliminar',
            confirm: {
                _: '¿Está seguro que desea eliminar %d filas?',
                1: '¿Está seguro que desea eliminar 1 fila?',
            },
        },
        error: {
            system:
            'Ha ocurrido un error en el sistema (<a target="\\" rel="\\ nofollow" href="\\">Más información&lt;\\/a&gt;).</a>',
        },
        multi: {
            title: 'Múltiples Valores',
            info: 'Los elementos seleccionados contienen diferentes valores para este registro. Para editar y establecer todos los elementos de este registro con el mismo valor, hacer click o tap aquí, de lo contrario conservarán sus valores individuales.',
            restore: 'Deshacer Cambios',
            noMulti:
            'Este registro puede ser editado individualmente, pero no como parte de un grupo.',
        },
        },
        info: 'Mostrando _START_ a _END_ de _TOTAL_ registros',
        stateRestore: {
        creationModal: {
            button: 'Crear',
            name: 'Nombre:',
            order: 'Clasificación',
            paging: 'Paginación',
            search: 'Busqueda',
            select: 'Seleccionar',
            columns: {
                search: 'Búsqueda de Columna',
                visible: 'Visibilidad de Columna',
            },
            title: 'Crear Nuevo Estado',
            toggleLabel: 'Incluir:',
        },
        emptyError: 'El nombre no puede estar vacio',
        removeConfirm: '¿Seguro que quiere eliminar este %s?',
        removeError: 'Error al eliminar el registro',
        removeJoiner: 'y',
        removeSubmit: 'Eliminar',
        renameButton: 'Cambiar Nombre',
        renameLabel: 'Nuevo nombre para %s',
        duplicateError: 'Ya existe un Estado con este nombre.',
        emptyStates: 'No hay Estados guardados',
        removeTitle: 'Remover Estado',
        renameTitle: 'Cambiar Nombre Estado',
        },
    },
    };

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await cita_detalle();

    dataTable = $("#datatable-cita").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
    console.log("Tabla de citas inicializada correctamente.");
};
    
const cita_detalle = async () => {
    try {
        const response = await fetch("https://la-eterna-primavera.onrender.com/cita_detalle/");
        const data = await response.json();
        console.log(data);

        if (!Array.isArray(data.Citas)) {
            console.error("Error: data.Citas no es un array");
            return;
        }
        let content = ``;
        data.Citas.forEach((Cita, list_cita) => {
            content += `
                <tr data-cita_id="${Cita.id || ''}">
                    <td>${list_cita + 1}</td>
                    <td>${Cita.nombre_paciente}</td>
                    <td>${Cita.apellido_paciente}</td>
                    <td>${Cita.servicio}</td>
                    <td>${Cita.fecha_cita}</td>
                    <td>${Cita.hora_cita}</td>
                    <td>${Cita.tipo_consulta}</td>
                    <td><i class="fa-solid fa-circle-check"></i></td>
                    <td>
                    
                </tr>`;
        });


        tableBody_cita.innerHTML = content;

        $(".editar").on("click", function () {
            const citaId = $(this).closest("tr").data("cita_id");
            console.log("Cita ID (antes de eliminarCita):", citaId);
            if (citaId) {
                window.location.href = `https://la-eterna-primavera.onrender.com/edit_citas/${citaId}/`;
            } else {
                console.error("No se pudo obtener el ID de la cita.");
            }
        });

        $(".btn-eliminar").on("click", async function () {
            try {
                const trElement = $(this).closest('tr');
                console.log("trElement:", trElement);

                const citaId = trElement.data('cita_id');
                console.log("Cita ID antes de la solicitud AJAX:", citaId);

                if (citaId !== undefined && citaId !== "") {
                    console.log("Antes de eliminarCita - Cita ID válido:", citaId);
                    if (confirm("¿Estás seguro de eliminar esta cita?")) {
                        await eliminarCita(citaId);
                    }
                } else {
                    console.error("El ID de la cita no es válido.");
                }
            } catch (error) {
                console.error('Error al eliminar cita:', error);
            }
        });

    } catch (error) {
        alert(error);
    }
};
    
const eliminarCita = async (citaId) => {
    console.log("Cita ID antes de la solicitud AJAX:", citaId);

    try {
        const csrfToken = obtenerCsrfToken(); // Asegúrate de obtener el token CSRF de la manera correcta
        if (citaId !== undefined && citaId !== "") {
            console.log("Antes de eliminarCita - Cita ID válido:", citaId);
            if (confirm("¿Estás seguro de eliminar esta cita?")) {
                const response = await $.ajax({
                    url: `https://la-eterna-primavera.onrender.com/eliminar_cita/${citaId}/`,
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken,
                    },
                });

                // Puedes imprimir la respuesta del servidor en la consola para obtener más información
                console.log('Respuesta del servidor:', response);

                // Actualiza la tabla después de eliminar la cita si es necesario
                await initDataTable();
            }
        } else {
            console.error("El ID de la cita no es válido.");
        }
    } catch (error) {
        console.error('Error al eliminar cita:', error);
    }
};

window.addEventListener('load', async () => {
    await initDataTable();
    await cita_detalle();
});