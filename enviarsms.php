<?php
$vgnumerr = "";
$vgerror = "";
$vgdest = "";
//$vgxml = "";

function enviarsms($parServicio, $parEmisor, $parLogin, $parPwd, $parRef, $parFechaEnv, $parHoraEnv, $parPc, $parMsg, $parDest) {
	global $vgerror;
	//global $vgxml;

	$envio = "N";
	$key = md5($parServicio.";csms@auto;".$parEmisor.";".$parLogin.";".$parPwd.";".$parRef);
	
	//Xml
	$xml = '<?xml version="1.0" encoding="ISO-8859-1"?>';
	$xml .= '<enviar Servicio="'.$parServicio.'" Emisor="'.$parEmisor.'" Login="'.$parLogin.'" Pwd="'.$parPwd.'" NumDest="1" Referencia="'.$parRef.'" FechaEnv="'.$parFechaEnv.'" HoraEnv="'.$parHoraEnv.'" NombrePC="'.$parPc.'" Key="'.$key.'">';
	$xml .= '<Mensaje>' . $parMsg . '</Mensaje>';
	$xml .= '<Dest>' . $parDest . '</Dest>';
	$xml .= '</enviar>';

	$xmlres = HTTPrequest("POST", "157.100.84.58", "/contactosms/wclsContactoSMS.aspx", $xml);	

	$posdata = strpos($xmlres, "\r\n\r\n");
	if ($posdata === false) { $vgerror = "Documento XML Invalido: ".$xmlres; }
	else {
		$xmlres = substr($xmlres, $posdata+2);
		//$vgxml = $xmlres;
		XMLParse($xmlres); 
	}
}

function HTTPrequest($method, $host, $usepath, $postdata = "") {  

    if(is_array($postdata)) { 
          foreach($postdata as $key=>$val) { 
              if(!is_integer($key)) { $data .= "$key=".urlencode($val)."&"; }
          } 
     } else { 
          $data = $postdata; 
     }

     $fp = pfsockopen( $host, 80, $errno, $errstr, 120);  
	//$fp = fsockopen( $host, 17980, &$errno, &$errstr, 120);  

      
     if( !$fp ) {  
        $output = '<resenviar Errores="1"><Error Dest="0">'.$errstr.'('.$errno.')</Error></resenviar>';
     } 
     else {
	     if( strtoupper($method) == "GET" ) {  
        	    fputs( $fp, "GET $usepath HTTP/1.0\n");  
	     }  
	     else if( strtoupper($method) == "POST" ) {  
        	    fputs( $fp, "POST $usepath HTTP/1.0\n");  
	     }  
     
	     fputs( $fp, "Accept: */*\n");  
	     fputs( $fp, "Accept: image/gif\n");  
	     fputs( $fp, "Accept: image/x-xbitmap\n");  
	     fputs( $fp, "Accept: image/jpeg\n");  
     
	     if( strtoupper($method) == "POST" ) {  
	            $strlength = strlen( $postdata); 
	            fputs( $fp, "Content-type: text/xml\n");  
	            fputs( $fp, "Content-length: ".$strlength."\n\n");  
	            fputs( $fp, $postdata."\n");  
	     } 

	     fputs( $fp, "\n" , 1);  
	     $output = "";   
	     stream_set_timeout($fp, 60);
	     while( !feof( $fp ) ) {  			
	            $output .= fgets( $fp, 1024);  
	     }  
	     $info = stream_get_meta_data($fp);
	     fclose( $fp); 
	     if ($info['timed_out']) {
           $output = '<resenviar Errores="1"><Error Dest="0">Tiempo de espera agotado.</Error></resenviar>';
    		} 
 
     }  
     return $output;  
}

function XMLParse($xml) {
	global $vgerror;
	global $vgnumerr;
	global $vgdest;

	$xml_parser = xml_parser_create();
	xml_parse_into_struct($xml_parser, $xml, $vals, $idxs);

	if (array_key_exists('ENVIO', $idxs)) {
		if (array_key_exists(0, $idxs['ENVIO'])) {
			if (array_key_exists('attributes', $vals[$idxs['ENVIO'][0]])) {
				if (array_key_exists('ERRORES', $vals[$idxs['ENVIO'][0]]['attributes'])) {
					$vgnumerr = $vals[$idxs['ENVIO'][0]]['attributes']['ERRORES'];
				}
			}
		}
	} else {
		if (array_key_exists('RESENVIAR', $idxs)) {
			if (array_key_exists(0, $idxs['RESENVIAR'])) {
				if (array_key_exists('attributes', $vals[$idxs['RESENVIAR'][0]])) {
					if (array_key_exists('ERRORES', $vals[$idxs['RESENVIAR'][0]]['attributes'])) {
						$vgnumerr = $vals[$idxs['RESENVIAR'][0]]['attributes']['ERRORES']; 
					}
				}
			}
		}
	}

	if (array_key_exists('ERROR', $idxs)) {
		if (array_key_exists(0, $idxs['ERROR'])) {
			if (array_key_exists('attributes', $vals[$idxs['ERROR'][0]])) {
				if (array_key_exists('DEST', $vals[$idxs['ERROR'][0]]['attributes'])) {
					$vgdest = $vals[$idxs['ERROR'][0]]['attributes']['DEST'];
				}
			}
			if (array_key_exists('value', $vals[$idxs['ERROR'][0]])) {
				$vgerror = $vals[$idxs['ERROR'][0]]['value'];
			}
		}
	} else {
		if (array_key_exists('OK', $idxs)) {
			$vgnumerr = "0";
			if (array_key_exists(0, $idxs['OK'])) {
				if (array_key_exists('attributes', $vals[$idxs['OK'][0]])) {
					if (array_key_exists('DEST', $vals[$idxs['OK'][0]]['attributes'])) {
						$vgdest = $vals[$idxs['OK'][0]]['attributes']['DEST'];
					}
				}
				if (array_key_exists('value', $vals[$idxs['OK'][0]])) {
					$vgerror = $vals[$idxs['OK'][0]]['value'];
				}
			}
		}
	}

	xml_parser_free($xml_parser);	
}

function respuestasms(&$numerr, &$dest, &$error,&$xml) {
	global $vgerror;
	global $vgnumerr;
	global $vgdest;
	//global $vgxml;

	$numerr = $vgnumerr;
	$dest = $vgdest;
	$error = $vgerror;
	//$xml = $vgxml;
	
}


?>