--UNIDAD 3: TRIGGERS: GUIA 12:
--CASO 1:
INSERT INTO transaccion_tarjeta_cliente VALUES(29320393064,
                                               1001,
                                               '04/05/2023',
                                               800000,
                                               24,
                                               845000,
                                               101);
INSERT INTO transaccion_tarjeta_cliente VALUES(29320393064,
                                               1002,
                                               '25/05/2023',
                                               86500,
                                               6,
                                               90325,
                                               101);
INSERT INTO transaccion_tarjeta_cliente VALUES(29320393064,
                                               1003,
                                               '25/05/2023',
                                               485900,
                                               12,
                                               544490,
                                               103);
INSERT INTO transaccion_tarjeta_cliente VALUES(28418181488,
                                               1002,
                                               '15/05/2023',
                                               200000,
                                               10,
                                               215000,
                                               102);
/
--trigger 
CREATE OR REPLACE TRIGGER trg_cupos
AFTER INSERT ON transaccion_tarjeta_cliente
FOR EACH ROW 
BEGIN 
    IF :NEW.cod_tptran_tarjeta IN (101,102) THEN
        UPDATE tarjeta_cliente 
        SET cupo_disp_compra = cupo_disp_compra - :NEW.monto_total_transaccion
        WHERE nro_tarjeta = :NEW.nro_tarjeta;
    ELSIF :NEW.cod_tptran_tarjeta = 103 THEN
        UPDATE tarjeta_cliente 
        SET cupo_disp_sp_avance = cupo_disp_sp_avance - :NEW.monto_total_transaccion
        WHERE nro_tarjeta = :NEW.nro_tarjeta;
    END IF;
END trg_cupos;
/
SELECT * FROM tarjeta_cliente WHERE nro_tarjeta IN (29320393064,28418181488)
--CASO 2:
/

INSERT INTO transaccion_tarjeta_cliente VALUES(31221815820,
                                               1004,
                                               '25/05/2023',
                                               900000,
                                               24,
                                               945000,
                                               102);
INSERT INTO transaccion_tarjeta_cliente VALUES(27516439752,
                                               1001,
                                               '21/05/2023',
                                               76500,
                                               1,
                                               80325,
                                               101);
INSERT INTO transaccion_tarjeta_cliente VALUES(27516439752,
                                               1002,
                                               '25/05/2023',
                                               585900,
                                               12,
                                               644490,
                                               103);
DELETE FROM transaccion_tarjeta_cliente
WHERE nro_tarjeta = 32623309887 AND cod_tptran_tarjeta = 103;
/
CREATE OR REPLACE TRIGGER trg_puntos
AFTER INSERT OR DELETE ON transaccion_tarjeta_cliente
FOR EACH ROW
DECLARE
    v_run NUMBER;
BEGIN
    IF INSERTING THEN
        SELECT tc.numrun 
        INTO v_run
        FROM tarjeta_cliente tc 
        WHERE :NEW.nro_tarjeta = tc.nro_tarjeta;
        UPDATE pesos_circulo_cencofalrip
        SET pesos_acumulados = pesos_acumulados + ROUND(0.5/100 * :NEW.monto_transaccion),
            fecha_actualizacion = :NEW.fecha_transaccion
        WHERE numrun =  v_run;
        
        IF SQL%ROWCOUNT = 0 THEN 
            INSERT INTO pesos_circulo_cencofalrip
            VALUES (v_run, ROUND(0.5/100 * :NEW.monto_transaccion), :NEW.fecha_transaccion);
        END IF;
    ELSIF DELETING THEN 
        SELECT tc.numrun 
        INTO v_run
        FROM tarjeta_cliente tc 
        WHERE :OLD.nro_tarjeta = tc.nro_tarjeta;
        
        UPDATE pesos_circulo_cencofalrip
        SET pesos_acumulados = pesos_acumulados - ROUND(0.5/100 * :OLD.monto_transaccion)
        WHERE numrun = v_run;
    END IF;
    
END trg_puntos;



import numpy as np

# Crear un arreglo de 3 filas por 3 columnas con ceros
arreglo = np.zeros((3, 3))

# Recorrer filas y elementos del arreglo
for fila in arreglo:
    for elemento in fila:
        print(int(elemento), end=' ')
    print()
