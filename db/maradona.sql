CREATE DATABASE IF NOT EXISTS `maradona` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
USE `maradona`;

# Volcado de tabla frases
# -----------------------------------------------------------

DROP TABLE IF EXISTS `frases`;

CREATE TABLE `frases` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `frase` varchar(1000) NOT NULL,
  `detalle` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf-8;

INSERT INTO `frases` (`frase`, `detalle`)
VALUES
	('Mis sueños son dos. Mi primer sueño es jugar en el Mundial, y el segundo es salir campeón de Octava y lo que siga en el campeonato este (con Argentinos)','De cuando era un niño en las Inferiores del Bicho, ésa fue la primera expresión que trascendió el paso del tiempo y que incluso se sacó de contexto: durante décadas la frase se pasó cortada hasta la palabra "campeón", como si se refiriera a la Copa del Mundo, pero Diego (Dieguito) hablaba del torneo que estaba disputando en Juveniles.'),
  ('Ganarle a River es como que tu mamá te venga a despertar con un beso a la mañana','La sensación única de ganar un superclásico, en palabras del Diez...'),
  ('Pensé que venía Berlusconi y me encontré con el cartonero Báez','Probablemente la frase más recordada de su primera etapa de enfrentamientos con Mauricio Macri, por entonces el presidente de Boca: en ese momento, cuando contrataba a Bilardo para ser el DT, también reducía las primas del plantel.'),
  ('Se le escapó la tortuga','Viene de una anécdota desopilante con James Cheek, el ex embajador estadounidense en Argentina, cuando mandó a buscar una tortuga que se le había perdido al hijo en un campo de 3.000 hectáreas.'),
	('Me siento más sólo que Kung Fu','Durante sus días en Cuba, Diego describía así sus sensaciones.'),
	('Lástima no se le tiene a nadie, maestro. Pelealo, tenele bronca, pero lástima a nadie','De invitado en El Equipo de Primera, con Fernando Niembro, tiró otra de sus frases célebres, dirigida a José Sanfilippo: el Nene discutía fuerte con Ruggeri y Veira, al punto que le dijo al Bambino que le daba lástima. Y lástima, dijo Diego, a nadie: la tribuna se vino abajo.'),
	('¿Que el hincha se muere por un abrazo entre Maradona y Riquelme? No. Decile que se va a quedar vivo','Antes de la última fecha del campeonato pasado los periodistas le decían que la gente se moría por ver a los dos ídolos juntos, y él salió a lo Maradó...');

UNLOCK TABLES;
